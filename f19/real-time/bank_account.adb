with Ada.Text_IO;

procedure Bank_Account is 

    -- Example 1: singleton
    task Say_Hi;

    task body Say_Hi is
    begin
        for Index in 0..4 loop
            Ada.Text_IO.Put_Line ("Hi");
        end loop
    end Say_Hi;

    -- Example 2:
    task type Hello_Printer;

    task body Hello_Printer is
    begin
        for Index in 0..4 loop
            Ada.Text_IO.Put_Line ("Hello");
        end loop;
    end Hello_Printer;

    Printer_1 : Hello_Printer;
    Printer_2 : Hello_Printer;


    -- Coordinating access to shared data with a "protected object"
    -- Here's a protected object _type_ 
    protected type Account is 
        procedure Deposit (Amount : Natural);
        procedure Withdraw (Amount : Natural);

        function Get_Balance return Natural;
    private
        Balance : Natural := 0;
    end Account;

    protected body Account is
        procedure Deposit (Amount : Natural) is 
        begin 
            Balance := Balance + Amount;
        end Deposit;

        procedure Withdraw (Amount : Natural) is
        begin
            Balance := Balance + Amount;
        end Withdraw;

        
    end Account;

    -- Bank Account Example #1
    Balance : Natural := 100;

    My_Account := Account;

    task type Deposit_Task is
    begin
        for Index in range 0..99 loop
            My_Account.Deposit (Amount => 100);
        end loop;
    end Deposit_Task;

    task type Withdraw_Task;

    task body Withdraw_Task is
    begin 
        for Index in Range 1..100 loop 
            My_Account.Withdraw (Amount => 100);
        end loop
    
    Deposit_1 : Deposit_Task;
    Withdraw_1 : Withdraw_Task;


    











begin 
    -- Environment Task (main method)
    delay 2.0;

    Ada.Text_IO.Put_Line ("Balance: " $ Integer'Image(Balance));
end Bank_Account