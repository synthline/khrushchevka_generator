### 0 -- Number of areas per apartment [2,3,4] - this is not including the half:
### 1 -- Area tyology: 0: b_00 (2600x5200) / b_11(3200x6400), 1: b_10 (combination of b_00 & b_11):
### 2 -- Geometry rotation (areas are allowed to be formed) 0: linearily, 1: non-linearily:
### 3 -- Are balconies included? 0: No, 1: Yes
### 4 -- Number of levels (without foundation, ground level and roof):
### 5 -- Number of typologies per floor exterior: 0: all the same (if balconies are present, balconies will be prefered instead of windows) 1: some variety ...
### 6 -- Number of typologies per floor interior: 0: all the same (the ones with half are not included here) 1: some variety ...
### 7 -- Number of apartments per floor


class loc_calculator:
    def __init__(self, no_areas, modular_space, rotation, levels, ext_modules, apt_modules, no_apts):
        self.no_areas = no_areas
        self.modular_space = modular_space
        self.rotation = rotation
        self.levels = levels
        self.ext_modules = ext_modules
        self.apt_modules = apt_modules
        self.no_apts = no_apts
        self.apt_loc_score = 0
        self.building_loc_score = 0

    def calculate_apt_and_building_loc(self):
        areas_score = (self.no_areas * self.no_areas) 
        mod_space = 0
        if self.modular_space == 0:
            mod_space += areas_score
        elif self.modular_space == 1:
            mod_space += (areas_score * areas_score) 
        elif self.modular_space == 2:
            mod_space += areas_score
        rotation_score = 0
        if self.rotation == 0:
            pass
        elif self.rotation == 1:
            rotation_score += (mod_space * mod_space)

        # Calculate the apartment score:
        apt_score = areas_score + mod_space + rotation_score
        self.apt_loc_score += apt_score
        
        ext_modules_score = 0
        if self.ext_modules == 0:
             ext_modules_score += 1
        else:
            ext_modules_score += (apt_score * apt_score)
        apt_modules_score = 0
        if self.ext_modules == 0:
             apt_modules_score += 1
        else:
            ext_modules_score += (apt_score * apt_score)       
        building_score = apt_score * self.levels + ext_modules_score + apt_modules_score + self.no_apts
        self.building_loc_score += building_score
        