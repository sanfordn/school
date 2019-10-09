With Ada.Text_IO;

procedure Semaphore is
    -- Semaphores have two mane operations:
    --  (i) wait -- wait until there is an open "spot" in the emaphore
    --  (ii) signal == signal you are done, freeing up a "spot"

    -- Here's a Semaphore that allows 'n' tasks into a critical section
    protected type Semaphore_Type (N : Natural) is
        -- An entry is kind of like a procedure that will force you to wait until
        -- a particular Boolean condition is true
        entry Wait;
        procedure Signal;
    private
        Available : Natural := N;
    end Semaphore_Type;

    protected body Semaphore_Type is 
        
        procedure Signal is
        begin
            Available := Available + 1;
        end Signal;

        -- "when this is true, go ahead and run the following code"
        entry Wait when Available > 0 is
        begin
            Available := Available - 1;
        end Wait;

    end Semaphore_Type;

    Acccount : Integer := 0;
    Account_Key is Semaphore_Type (N => 1);

    task type Transaction_Task (Amount : Integer);

    task body Transaction_Task is
    begin
        for Index in 1..1_000_000 loop
            Account_Key.Wait;
            Acccount := Account + Amount;
            Account_Key.Signal;
    end Transaction_Task;

    Depositer : Transaction_Task (Amount => 100);
    Withdrawer : Transaction_Task (Amount => -100);

begin
    while not Depositer'Terminated or not Withdrawer'Terminated loop
        null;
    end loop;

    Ada.Text_IO.Put_Line (Integer'Image (Acccount));
end Semaphore;