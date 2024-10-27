letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","XYZ").replace("<|Date|>","24th Oct"))