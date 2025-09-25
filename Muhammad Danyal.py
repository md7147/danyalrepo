#Name:Muhammad Danyal ID: 413002535
def Triangle_Type_Checker():
    SideA = int(input("Enter Side 1="))
    SideB = int(input("Enter Side 2="))
    SideC = int(input("Enter Side 3="))
    """Checks whether the Triangle is Equilateral."""
    
    if SideA==SideB and SideB==SideC:                    #Function to check if triangle is Equilateral
        print("This Triangle is Equilateral")
        """Checks whether the Triangle is Isosceles."""

    elif SideA==SideB or SideB==SideC or SideC==SideA:    #Function to check if triangle is Isosceles
        print("Isosceles triangle")
        """Checks whether the Triangle is Scalene."""
                                                          #Function to check if triangle is Scalene
    else:print("Scalene triangle")    


Triangle_Type_Checker()




