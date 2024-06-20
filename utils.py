class ImageCheck:
    
    @staticmethod
    def is_image_ext_valid(src_path: str) -> bool:
        valid_exts = ['png', 'jpg', 'jpeg']
        try:
            return src_path[src_path.rfind('.') + 1:] in valid_exts
        except:
            return False
    
    @staticmethod
    def is_file_image(src_path) -> bool:
        return False