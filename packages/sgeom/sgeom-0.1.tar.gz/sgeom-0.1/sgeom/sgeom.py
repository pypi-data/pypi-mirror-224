# Copyright (C) 2023 Juncheng E, Mats Fangohr
# Contact: Juncheng E <juncheng.e@xfel.eu>
# This file is part of sgeom which is released under MIT License.

import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from scipy.spatial.transform import Rotation
from typing import Union


# Define the colors for the binary colormap
color1 = "blue"
color2 = "red"

# Define the boundary value to split the colormap
boundary_value = 0.0

# Create a binary colormap with the specified colors
cmap_binary = ListedColormap([color1, color2])

# Create a BoundaryNorm to specify the boundary value
norm = BoundaryNorm([0, boundary_value, 1], cmap_binary.N)


class sgeom:
    """
    Class to handle the geometry of pixels of a detector.

    Args:
        pixels_lab (ndarray): ndarray of pixel positions (vertical, horizontal) in meters, shape (-1, 3).
        clen (float): Distance between the sample and the PONI in meters.
        pixel_size (tuple[float]): The size of a single pixel ([height, width]) in meters. if they are the same, a float input is allowed.
        X1 (tuple, optional): The X1 axis in lab system toward the ceiling, expressed in sample coordinates. Defaults to sample (0, 0, 1).
        X2 (tuple, optional): The X2 axis in lab system transverse to the incident beam, expressed in sample coordinates. Defaults to sample (1, 0, 0).
        X3 (tuple, optional): The X3 axis in lab system along the beamline toward the detector in sample coordinates. Defaults to sample (0, 1, 0).
        wavelength (float, optional): The wavelength of the beam in meters. Defaults to 1.33e-10 (12.398/9.3 KeV).
        d1_hat_lab (tuple, optional): The d1 detector axis along the vertical direction in lab system. Defaults to (1, 0, 0).
        d2_hat_lab (tuple, optional): The d2 detector axis along the horizontal direction in lab system. Defaults to (0, 1, 0).
        d3_hat_lab (tuple, optional): The d3 detector axis away from the sample in lab system. It relates to PONI and beam_center Defaults to (0, 0, 1).
        beam_vec_lab (tuple, optional): The exact beam vector [X1, X2, X3] in lab system. The default is [0, 0, 1], i.e. along the X3 axis.
    """

    def __init__(
        self,
        pixels_lab: ndarray,
        clen: float,
        pixel_size: Union[float, tuple],
        X1: tuple = (0, 0, 1),
        X2: tuple = (1, 0, 0),
        X3: tuple = (0, 1, 0),
        wavelength: float = 1.33e-10,
        d1_hat_lab: tuple = (1, 0, 0),
        d2_hat_lab: tuple = (0, 1, 0),
        d3_hat_lab: tuple = (0, 0, 1),
        beam_vec_lab: tuple = (0, 0, 1),
    ):
        self._generate_basis_vectors(X1, X2, X3)

        # Make sure it's unit vector
        self.d1_hat_lab = np.array(d1_hat_lab) / np.linalg.norm(d1_hat_lab)
        self.d2_hat_lab = np.array(d2_hat_lab) / np.linalg.norm(d2_hat_lab)
        self.d3_hat_lab = np.array(d3_hat_lab) / np.linalg.norm(d3_hat_lab)

        assert isinstance(clen, float) or isinstance(
            clen, int
        ), "`clen` must be a number in meters."
        self.clen = clen

        # PONI in lab is always along d3_hat_lab direction.
        self.poni_lab = self.d3_hat_lab * clen

        if not isinstance(pixel_size, (tuple, list, ndarray)):
            pixel_size = (pixel_size, pixel_size)
        assert len(pixel_size) == 2, "Pixels can only have a size in 2 dimensions."
        self.pixel_size = np.array(pixel_size)

        self.wavelength = wavelength

        # assert detector_pixels.shape[-1] == 2
        # self.detector_pixels = detector_pixels
        # self.pixels_lab = self._offset_in_lab(pixels_lab)
        self.pixels_lab = pixels_lab

        # unit direction vector
        self.beam_hat_lab = np.array(beam_vec_lab) / np.linalg.norm(beam_vec_lab)
        self.set_beam_center_lab(self.beam_hat_lab)
        self.lab_to_sample()
        self.sample_to_reciprocal()

    def info(self):
        strings = "Scattering geometry:\n"
        strings += f"number of detector pixels: {self.npixels}\n"
        strings += f"Pixel size [V, H]: {self.pixel_size}\n"
        strings += f"Sample to detector distance: {self.clen} m\n"
        strings += f"PONI in lab: [0, 0, {self.clen}], unit: m\n"
        strings += "PONI on detector [d1, d2]: [0, 0], \n\n"
        strings += "Lab axes in sample system (x, y ,z):\n"
        strings += f"X1 = {self.X1_hat}\n"
        strings += f"X2 = {self.X2_hat}\n"
        strings += f"X3 = {self.X3_hat}\n\n"
        strings += "Detector axes in lab system:\n"
        strings += f"d1_hat_lab = {self.d1_hat_lab}\n"
        strings += f"d2_hat_lab = {self.d2_hat_lab}\n"
        strings += f"d3_hat_lab = {self.d3_hat_lab}\n\n"
        strings += "Beam:\n"
        strings += f"Wavelength = {self.wavelength:g} m\n"
        strings += f"Photon energy = {12.398/(self.wavelength*1e10)} keV\n"
        strings += f"Beam vector in lab [X1, X2, X3] = {self.beam_hat_lab}\n"
        strings += (
            f"Beam center in lab [X1, X2, X3] = {self.beam_center_lab}, unit: m\n"
        )
        strings += (
            f"Beam center on detector [d1, d2] = {self.beam_center_det}, unit: pixel\n"
        )
        strings += "Reciprocal space, unit=1/m:\n"
        strings += (
            "1/resolution: sgeom.qspace and 3D reciprocal space map: sgeom.reciprocal\n"
        )
        strings += f"Resolution at corner = {1./self.qspace.max()*1e10:.3f} Angstrom\n"
        print(strings)

    def __check_orthogonal(self, in_tuple: tuple):
        """Check if the vectors an input tuple are orthogonal to each other, if not, give some suggestions."""
        if is_orthogonal(in_tuple):
            pass
        else:
            suggestions = suggest_orthogonal(in_tuple)
            strings = ""
            for suggestion in suggestions:
                for i in range(len(suggestion)):
                    suggestion[i] = tuple(suggestion[i])
                strings += str(suggestion) + "\n"
            raise ValueError(
                f"{in_tuple} is not orthogonal, try the following:\n{strings}"
            )

    def _generate_basis_vectors(self, X1, X2, X3):
        """
        Generates the vectors needed for conversions between systems.
        The lab axis unit vectors in sample system.
        Lab origin and sample origin are the same.

        Args:
            X1 (tuple): The X1 axis in lab system toward the ceiling, expressed in sample coordinates.
            X2 (tuple): The X2 axis in lab system transverse to the incident beam, expressed in sample coordinates.
            X3 (tuple): The X3 axis in lab system along the incident beam toward the detector in sample coordinates. It defines the beam direction with respect to the sample system.
        """
        self.__check_orthogonal([X1, X2, X3])
        self.X1_hat = np.array(X1) / np.linalg.norm(X1)  # sample z
        self.X2_hat = np.array(X2) / np.linalg.norm(X2)  # sample x
        self.X3_hat = np.array(X3) / np.linalg.norm(X3)  # sample y

    def plot_lab(self):
        """Plot coordinate map of the detector in lab system, unit: meter."""

        PONI = find_positon(self.pixels_lab, 0, 0)
        print(PONI)
        beam_loc = find_positon(
            self.pixels_lab,
            self.beam_center_lab[0],
            self.beam_center_lab[1],
        )

        plot_with_mark(
            self.pixels_lab[..., 0], "Vertical direction", [PONI[1], PONI[0]]
        )
        plt.scatter(
            beam_loc[1],
            beam_loc[0],
            marker="o",
            facecolors="none",
            edgecolors="r",
            s=150,
            label="Beam center",
        )
        plt.legend()

        plot_with_mark(
            self.pixels_lab[..., 1], "Horizontal direction", [PONI[1], PONI[0]]
        )
        plt.scatter(
            beam_loc[1],
            beam_loc[0],
            marker="o",
            facecolors="none",
            edgecolors="r",
            s=150,
            label="Beam center",
        )
        plt.legend()
        # plt.imshow(
        #     self.pixels_lab[..., 1],
        #     origin="lower",
        #     cmap=cmap_binary,
        #     interpolation="nearest",
        #     norm=norm,
        # )
        # cbar = plt.colorbar(ticks=[0, boundary_value, 1])
        # cbar.ax.set_yticklabels(
        #     [str(0), str(boundary_value), str(1)]
        # )  # Custom tick labels

    @property
    def reciprocal(self):
        """The reciprocal space mesh"""
        return self._reciprocal

    @property
    def qspace(self):
        """The qspace mesh"""
        return self._qspace

    @property
    def npixels(self):
        """Number of pixels"""
        return self.pixels_lab.reshape(-1, 3).shape[0]

    # @property
    # def poni_lab(self):
    #     """PONI in lab system. It's a 3D vector."""
    #     return self._poni_lab

    # def _set_poni_lab(self):
    #     """Set the PONI lab coordinate"""

    # PONI in lab is always along d3_hat_lab direction.
    #     self._poni_lab = self.clen * self.d3_hat_lab

    def set_beam_center_lab(self, beam_hat_lab):
        # After offset detector in lab, PONI is already aligned to the origin of the sample/lab.
        beam_center_lab = get_beam_center_lab(beam_hat_lab, self.poni_lab)
        beam_center_on_d1 = np.dot(beam_center_lab, self.d1_hat_lab)
        beam_center_on_d2 = np.dot(beam_center_lab, self.d2_hat_lab)
        beam_center_on_d3 = np.dot(beam_center_lab, self.d3_hat_lab)
        beam_center_det_arr = np.array(
            [beam_center_on_d1, beam_center_on_d2, beam_center_on_d3]
        )
        assert beam_center_on_d3 - self.clen < 1e-9
        # self.beam_center_det = (beam_center_det_arr[:2] + self.poni) / self.pixel_size
        self.beam_center_det = beam_center_det_arr[:2] / self.pixel_size
        self.beam_center_lab = beam_center_lab

    def lab_to_sample(self):
        # try:
        #     pixels_lab = np.reshape(self.pixels_lab, (-1, 3))
        # except AttributeError:
        #     self.det_to_lab()
        pixels_lab = np.reshape(self.pixels_lab, (-1, 3))
        pixels_sample = np.dot(
            pixels_lab, np.array([self.X1_hat, self.X2_hat, self.X3_hat])
        )
        beam_center_sample = np.dot(
            self.beam_center_lab, np.array([self.X1_hat, self.X2_hat, self.X3_hat])
        )

        self.beam_center_sample = beam_center_sample
        self.pixels_sample = np.reshape(pixels_sample, self.pixels_lab.shape)

    def sample_to_reciprocal(self):
        coords = np.reshape(self.pixels_sample, (-1, 3))
        ewald_radius = 1 / self.wavelength
        k0 = (
            self.beam_center_sample
            / np.linalg.norm(self.beam_center_sample)
            * ewald_radius
        )
        ks = coords / np.linalg.norm(coords, axis=1)[:, np.newaxis] * ewald_radius
        reciprocal = ks - k0
        qspace = np.linalg.norm(reciprocal, axis=1)

        self._qspace = np.reshape(qspace, self.pixels_sample.shape[:-1])
        self._reciprocal = np.reshape(reciprocal, self.pixels_sample.shape)

    @classmethod
    def from_extra_geom_pixel_positions(
        cls,
        pixel_positions: ndarray,
        clen: float,
        pixel_size: Union[float, tuple],
        X1: tuple = (0, 0, 1),
        X2: tuple = (-1, 0, 0),
        X3: tuple = (0, 1, 0),
        **kwargs,
    ):
        """
        Method to create a sgeom instance from extra_geom.get_pixel_positions(). In extra_geom, the direction of
        the horizontal axis is in inverse to the lab/pyFAI convention.
        See https://extra-geom.readthedocs.io/en/latest/geometry.html and  https://pyfai.readthedocs.io/en/v2023.1/

        Args:
            pixel_positions (ndarray): The output of extra_geom.get_pixel_positions() in meters from center (0, 0). It's (0, 0) is treated as PONI. Shape (-1, 3).
            clen (float): Distance between the sample and the PONI in meters.
            pixel_size (tuple[float]): The size of a single pixel ([height, width]) in meters. if they are the same, a float input is allowed.
            X1 (tuple, optional): The X1 axis in lab system toward the ceiling, expressed in sample coordinates. Defaults to sample (0, 0, 1).
            X2 (tuple, optional): The X2 axis in lab system transverse to the incident beam, expressed in sample coordinates. Defaults to sample (1, 0, 0).
            X3 (tuple, optional): The X3 axis in lab system along the beamline toward the detector in sample coordinates. Defaults to sample (0, 1, 0).
            wavelength (float, optional): The wavelength of the beam in meters. Defaults to 1.33e-10 (12.398/9.3 KeV).
            beam_vec_lab (tuple, optional): The exact beam vector [X1, X2, X3] in lab system. The default is [0, 0, 1], i.e. along the X3 axis.
        """

        # The first column in extra_geom is x-axis while that in pyFAI is vertical axis. Here we do a conversion.
        pixel_positions[..., [1, 0]] = pixel_positions[..., [0, 1]]
        pixel_positions[..., 2] += clen

        return cls(pixel_positions, clen, pixel_size, X1=X1, X2=X2, X3=X3, **kwargs)

    @classmethod
    def from_pixel_number(
        cls,
        npixels: tuple[int],
        clen: float,
        poni: tuple[float],
        pixel_size: tuple[float],
        rot=(0, 0, 0),
        **kwargs,
    ):
        """
        Method to create a sgeom instance from number of pixels.

        Args:
            npixels (tuple[int]): Number of pixels in (vertical, horizontal) directions, e.g. (128, 128).
            clen (float): Distance between the sample and the PONI in meters.
            poni (tuple[float]): Point Of Normal Incidence coordinates in the detector system in pixel unit ([vertical, horizontal]) from the lower left.
            pixel_size (tuple[float]): The size of a single pixel ([height, width]) in meters.
            rot (tuple, optional): [rot1, rot2, rot3] in radians - see pyFAI geometry (https://pyfai.readthedocs.io/en/master/geometry_conversion.html#geometry-definition-of-pyfai for details. Defaults to (0, 0, 0).
            X1 (tuple, optional): The X1 axis in lab system toward the ceiling, expressed in sample coordinates. Defaults to sample (0, 0, 1).
            X2 (tuple, optional): The X2 axis in lab system transverse to the incident beam, expressed in sample coordinates. Defaults to sample (1, 0, 0).
            X3 (tuple, optional): The X3 axis in lab system along the beamline toward the detector in sample coordinates. Defaults to sample (0, 1, 0).
            wavelength (float, optional): The wavelength of the beam in meters. Defaults to 1.33e-10 (12.398/9.3 KeV).
            beam_vec_lab (tuple, optional): The exact beam vector [X1, X2, X3] in lab system. The default is [0, 0, 1], i.e. along the X3 axis.
        """
        assert len(rot) == 3

        if not isinstance(pixel_size, (tuple, list, ndarray)):
            pixel_size = (pixel_size, pixel_size)
        assert len(pixel_size) == 2, "Pixels can only have a size in 2 dimensions."
        pixel_size = np.array(pixel_size)

        # Detector axis unit vectors are initialized to be overlapped with the lab coordinate.
        d1_hat_lab = np.array([1, 0, 0])
        d2_hat_lab = np.array([0, 1, 0])
        d3_hat_lab = np.array([0, 0, 1])
        # It's not intuitive, but in accord with the pyFAI definition.
        detector_rotation = Rotation.from_rotvec(
            [[-rot[0], 0, 0], [0, -rot[1], 0], [0, 0, rot[2]]]
        )
        for rotation in detector_rotation:
            d1_hat_lab = rotation.apply(d1_hat_lab)
            d2_hat_lab = rotation.apply(d2_hat_lab)
            d3_hat_lab = rotation.apply(d3_hat_lab)
        assert is_orthogonal([d1_hat_lab, d2_hat_lab, d3_hat_lab])
        detector_pixels = get_detector_pixels(npixels)
        pixels_lab = det_to_lab(
            detector_pixels, pixel_size, poni, clen, d1_hat_lab, d2_hat_lab, d3_hat_lab
        )

        return cls(
            pixels_lab,
            clen,
            pixel_size,
            d1_hat_lab=d1_hat_lab,
            d2_hat_lab=d2_hat_lab,
            d3_hat_lab=d3_hat_lab,
            **kwargs,
        )


def det_to_lab(
    detector_pixels,
    pixel_size: tuple[float],
    poni,
    clen,
    d1_hat_lab,
    d2_hat_lab,
    d3_hat_lab,
):
    """Get the pixels in lab system and beam center in detector and beam center"""

    # astype is a copy https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html

    assert len(poni) == 2, "`poni` must be (vertical, horizontal) pixel unit"
    # Convert poni to its physical unit.
    # poni = np.array(poni) * np.array(pixel_size)
    pixels = np.reshape(detector_pixels.astype(float), (-1, 2))
    # Convert the unit to meter and define the detector in lab system.
    pixels[:, 0] = (pixels[:, 0] - poni[0]) * pixel_size[0]
    pixels[:, 1] = (pixels[:, 1] - poni[1]) * pixel_size[1]
    # Offset the pixels to the sample to detector distance
    clen_array = np.full((pixels.shape[0], 1), clen)
    pixels = np.concatenate((pixels, clen_array), axis=1)
    # PONI vector in detector system
    pixels_lab = np.dot(pixels, np.array([d1_hat_lab, d2_hat_lab, d3_hat_lab]))

    final_shape = list(np.shape(detector_pixels))
    final_shape[-1] = 3

    return np.reshape(pixels_lab, final_shape)


def get_detector_pixels(npixels: tuple):
    """
    Generate pixel coordinate array in shape (-1, 2).

    Args:
        npixels (tuple[int]): Number of pixels in (vertical, horizontal) directions, e.g. (128, 128).

    Returns:
        ndarray: Pixel coordinate array.
    """
    return np.moveaxis(np.indices((npixels[0], npixels[1])), 0, -1)


def get_beam_center_lab(beam_direction: tuple, sd_vector: tuple):
    """Get beam center in lab system from beam incident direction vector and sample to detector norm vector.
        Equation 14 in E, J. C. et al. Journal of Synchrotron Radiation 25, 604–611 (2018)
        doi:10.1107/S1600577517016733

    Args:
        beam_direction (tuple): Beam incident direction vector.
        sd_vector (tuple): Sample to detector norm vector, its length is sample to detector distance.

    Returns:
        ndarray: The dimension is the same as input.
    """
    beam_hat = np.array(beam_direction) / np.linalg.norm(beam_direction)
    return np.linalg.norm(sd_vector) ** 2 / np.dot(sd_vector, beam_hat) * beam_hat


def suggest_orthogonal(in_tutple: tuple):
    """Suggest a new vector if"""
    if len(in_tutple) != 3:
        raise ValueError("Input tuple/list must have 3 vectors")
    _, orthogonal_list = get_not_orthogonal_list(in_tutple)
    if len(orthogonal_list) == 0:
        raise ValueError(
            "None of the pairs are othogonal to each other, Please try a set with at least 2 othogonal vectors."
        )
    else:
        suggestion = []
        for pair in orthogonal_list:
            suggestion.append([pair[0], pair[1], orthogonal_from_two(pair[0], pair[1])])
        return suggestion


def orthogonal_from_two(v1, v2):
    """Get a vector that is orthogonal to the two input vectors"""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Input vectors must have 3 dimensions")

    # Convert the input vectors to NumPy arrays
    v1 = np.array(v1)
    v2 = np.array(v2)

    # Compute the cross product of the two input vectors
    orthogonal = np.cross(v1, v2)

    return orthogonal


def get_not_orthogonal_list(in_tuple: tuple):
    """Get a list of not orthogonal pairs of the input vector tuple/list.

    Args:
        in_tuple (tuple): The input tuple/list
    """
    not_orthogonal_list = []
    orthogonal_list = []
    pairs = get_pairs(in_tuple)
    for pair in pairs:
        if np.dot(pair[0], pair[1]) == 0:
            # It passes the orthogonal test
            orthogonal_list.append(pair)
        else:
            not_orthogonal_list.append(pair)
    return not_orthogonal_list, orthogonal_list


def is_orthogonal(in_tuple: tuple):
    """Check if the elements in a tuple/list are orthogonal to each other

    Args:
        in_tuple (tuple): The input tuple/list
    """
    not_orthogonal_list = get_not_orthogonal_list(in_tuple)[0]
    if len(not_orthogonal_list) == 0:
        return True
    else:
        print(f"{not_orthogonal_list} are not orthogonal")
        return False


def get_pairs(in_list):
    """Get pairs for the elements in a list."""
    pairs = []
    n = len(in_list)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((in_list[i], in_list[j]))
    return pairs


def plot_with_mark(pixels: ndarray, title: str, mark_pos: list, size=120):
    plt.figure()
    plt.imshow(
        pixels,
        origin="lower",
    )

    plt.colorbar()
    plt.scatter(
        mark_pos[0],
        mark_pos[1],
        marker="+",
        color="red",
        s=size,
        label="PONI",
    )
    plt.title(title)
    plt.legend()


def find_positon(TD_arr, val0, val1):
    PONI0 = np.where(TD_arr[..., 0] == val0)
    PONI1 = np.where(TD_arr[..., 1] == val1)
    PONI = np.intersect1d(PONI0[0], PONI1[0]), np.intersect1d(PONI0[1], PONI1[1])
    return PONI
