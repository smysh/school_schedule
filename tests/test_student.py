from school_schedule.student import Student
def test_student_initialization():
    #Arrange and Act
    samara = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )
    # Assert
    assert samara.name == "Samara"
    assert samara.grade == "junior"
    assert "Pre-Calc" in samara.classes 
    assert "English III" in samara.classes
    assert "World History" in samara.classes
    assert "Gym" in samara.classes
    assert "Chemistry" in samara.classes
    assert "Music Composition" in samara.classes
    assert len(samara.classes) == 6
    
def test_add_valid_class():
    #Arrange
    samara = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )
    #Act
    samara.add_class("Painting")
    # Assert
    assert len(samara.classes) == 7
    assert "Painting" in samara.classes