### 0 -- Number of areas per apartment [2,3,4] - this is not including the half:
### 1 -- Area tyology: 0: b_00 (2600x5200) / b_11(3200x6400), 1: b_10 (combination of b_00 & b_11):
### 2 -- Geometry rotation (areas are allowed to be formed) 0: linearily, 1: non-linearily:
### 3 -- Are balconies included? 0: No, 1: Yes
### 4 -- Number of levels (without foundation, ground level and roof):
### 5 -- Number of typologies per floor exterior: 0: all the same (if balconies are present, balconies will be prefered instead of windows) 1: some variety ...
### 6 -- Number of typologies per floor interior: 0: all the same (the ones with half are not included here) 1: some variety ...

class loc_calculator:
    def __init__(self, no_areas, modular_space, rotation, balconies, levels, ext_modules, apt_modules, no_apts):
        self.no_areas = no_areas
        self.modular_space = modular_space
        self.rotation = rotation
        self.balconies = balconies
        self.levels = levels
        self.ext_modules = ext_modules
        self.apt_modules = apt_modules
        self.no_apts = no_apts
        self.apt_loc_score = 0
        self.building_loc_score = 0


    def calculate_apt_and_building_loc():
        pass