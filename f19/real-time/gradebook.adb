package body Gradebook is
    -----------------
    -- Add_Student --
    -----------------
    procedure Add_Student (Gradebook : in out Grade_Roster_Rec;
                           Student_ID : in Student_ID_Type) is 
        Student_Info : Student_Rec;
    begin
        Gradebook.Size := Gradebook.Size + 1;
        Student_Info.Student_ID := Student_ID;
        Student_Info.Assignments := (others => (Points_Scored => 0, 
                                                Points_Possible => 0, 
                                                Work_Type => Quiz));
        Gradebook.Grades (Gradebook.Size) := (Student_Info);
    end Add_Student;
    ---------------------------
    -- Compute_Student_Grade --
    ---------------------------
    function Compute_Student_Grade (Gradebook : in Grade_Roster_Rec;
                                    Student_ID : in Student_ID_Type)
                                    return Float is
    begin

    end Compute_Student_Grade;
end Gradebook;
