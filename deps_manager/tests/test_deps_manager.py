import unittest
from unittest.mock import patch, MagicMock, mock_open
from deps_manager.src.dependencies import *
from deps_manager.src.main import *

class TestDependencyManager(unittest.TestCase):

    @patch('deps_manager.dependencies.subprocess.run')
    def test_install_dependencies_python(self, mock_subprocess_run):
        install_dependencies('python', 'requirements.txt')
        mock_subprocess_run.assert_called_once_with(['pip', 'install', '-r', 'requirements.txt'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_install_dependencies_cpp(self, mock_subprocess_run):
        install_dependencies('cpp', 'requirements.txt')
        mock_subprocess_run.assert_called_once_with(['conan', 'install', '-r', 'requirements.txt'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_uninstall_dependency_python(self, mock_subprocess_run):
        uninstall_dependency('python', 'package')
        mock_subprocess_run.assert_called_once_with(['pip', 'uninstall', '-y', 'package'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_uninstall_dependency_cpp(self, mock_subprocess_run):
        uninstall_dependency('cpp', 'package')
        mock_subprocess_run.assert_called_once_with(['conan', 'uninstall', '-y', 'package'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_list_dependencies_python(self, mock_subprocess_run):
        list_dependencies('python')
        mock_subprocess_run.assert_called_once_with(['pip', 'list'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_list_dependencies_cpp(self, mock_subprocess_run):
        list_dependencies('cpp')
        mock_subprocess_run.assert_called_once_with(['conan', 'list'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_update_dependencies_python(self, mock_subprocess_run):
        update_dependencies('python', 'requirements.txt')
        mock_subprocess_run.assert_called_once_with(['pip', 'install', '--upgrade', '-r', 'requirements.txt'], check=True)

    @patch('deps_manager.dependencies.subprocess.run')
    def test_update_dependencies_cpp(self, mock_subprocess_run):
        update_dependencies('cpp', 'requirements.txt')
        mock_subprocess_run.assert_called_once_with(['conan', 'update', '-r', 'requirements.txt'], check=True)


if __name__ == '__main__':
    unittest.main()
