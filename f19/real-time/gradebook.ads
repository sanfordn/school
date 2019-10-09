With Ada.Text_IO; Use Ada.Text_IO;  
With Ada.Integer_Text_IO; Use Ada.Integer_Text_IO;

package Gradebook is

    type Student_ID_Type is range 100_000..999_999;
    type Assignment_Type is (Homework, Quiz, Exam);

    type Assignment_Rec is 
        record
            Points_Scored : Natural;
            Points_Possible : Natural;
            Work_Type : Assignment_Type;
    type Student_Rec is
        record
            Student_ID : Student_ID_Type;
            Assignments : Assignment_Array;
            Size : Natural := 0;
        end record;

    type Assignment_Array is array (1..30) of Assignment_Rec;
    type Grade_Roster_Array is array (1..30) of Student_Rec;
    type Grade_Roster_Rec is 
        record
            Grades : Grade_Roster_Array;
            Size : Natural := 0;
        end record;

    procedure Add_Student (Gradebook : in out Grade_Roster_Rec;
                           Student_ID : Student_ID_Type);


end Gradebook;