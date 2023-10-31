import unittest
import os

def check_files_exist(directory):
    readme_exists = os.path.exists(os.path.join(directory, 'README.md'))
    license_exists = os.path.exists(os.path.join(directory, 'LICENSE'))
    
    return readme_exists, license_exists

class TestCheckFilesExist(unittest.TestCase):
    def test_check_files_exist(self):
        
        temp_dir = 'temp_test_dir'
        os.makedirs(temp_dir)
        
        
        with open(os.path.join(temp_dir, 'README.md'), 'w') as readme_file:
            readme_file.write('Sample README')
        
        with open(os.path.join(temp_dir, 'LICENSE'), 'w') as license_file:
            license_file.write('Sample License')
        
        
        readme_exists, license_exists = check_files_exist(temp_dir)
        
        self.assertTrue(readme_exists)
        self.assertTrue(license_exists)
        
    
        os.remove(os.path.join(temp_dir, 'README.md'))
        os.remove(os.path.join(temp_dir, 'LICENSE'))
        os.rmdir(temp_dir)

if __name__ == '__main__':
    unittest.main()
