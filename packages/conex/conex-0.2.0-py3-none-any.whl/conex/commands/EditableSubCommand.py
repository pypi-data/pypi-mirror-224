from .ConfigSubCommand import ConfigSubCommand
from ..internal.Utilities import Utilities


class EditableSubCommand:
    def __init__(self, conan, utils: Utilities, config: ConfigSubCommand):
        self._conan_editable = conan.editable
        self._utils = utils
        self._config = config

    def add(self, path_to_conanfile, path_to_layout=None):
        reference = self._utils.create_reference(path_to_conanfile)
        self._conan_editable.add(path_to_conanfile, reference, path_to_layout)

    def remove(self, path_to_conanfile):
        reference = self._utils.create_reference(path_to_conanfile)
        self._conan_editable.remove(reference)
