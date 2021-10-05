using System;
using System.Reflection.Metadata.Ecma335;

namespace Calculator
{
    public class Calculations
    {
        
        //Private Variables
        private double _firstNum;
        private double _secNum;
        private double _answer;
        private string _input = "";

        //Main Constructor
        public Calculations(double firstNum, double secNum, double answer)
        {
            _firstNum = firstNum;
            _secNum = secNum;
            _answer = answer;
        }

        //Default Contuctor
        public Calculations()
        {
            _firstNum = 0;
            _secNum = 0;
            _answer = 0;
        }
        
        //Public getter/setter for private variables
        public double FirstNum
        {
            get
            {
                return _firstNum;
            }
            set
            {
                _firstNum = value;
            }
        }

        //Different way of doing public getter/setter, still same thing
        public double SecNum
        {
            get => _secNum;
            set => _secNum = value;
        }

        public double Answer
        {
            get => _answer;
            set => _answer = value;
        }


        public void Addition()
        {
            Answer = FirstNum + SecNum;
            Console.WriteLine(Answer);
        }
        
        public void Subtraction()
        {
            Answer = FirstNum - SecNum;
            Console.WriteLine(Answer);
        }
        
        public void Multiplication()
        {
            Answer = FirstNum * SecNum;
            Console.WriteLine(Answer);
        }
        
        public void Division()
        {
            Answer = FirstNum / SecNum;
            Console.WriteLine(Answer);
        }
        
        //Caluclation Method
        public string Calculate()
        {
            Console.WriteLine("Let's Build a Calculator!");
            bool _exit = false;
            while (!_exit){
                Console.WriteLine("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n9. Exit");
                Console.WriteLine("\nPlease enter the menu number for your desired operation: ");
                _input = Console.ReadLine();
                
                switch (_input)
                {
                    case "1":
                        Console.WriteLine("You chose Addition!");
                        Console.WriteLine("Please enter your first number: ");
                        _firstNum = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter your second number: ");
                        _secNum = Convert.ToDouble(Console.ReadLine());
                        Calculations calculator1 = new Calculations(_firstNum, _secNum, _answer);
                        calculator1.Addition();
                        break;
                    case "2":
                        Console.WriteLine("You chose Subtraction!");
                        Console.WriteLine("Please enter your first number: ");
                        _firstNum = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter your second number: ");
                        _secNum = Convert.ToDouble(Console.ReadLine());
                        Calculations calculator2= new Calculations(_firstNum, _secNum, _answer);
                        calculator2.Subtraction();
                        break;
                    case "3":
                        Console.WriteLine("You chose Multiplication!");
                        Console.WriteLine("Please enter your first number: ");
                        _firstNum = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter your second number: ");
                        _secNum = Convert.ToDouble(Console.ReadLine());
                        Calculations calculator3 = new Calculations(_firstNum, _secNum, _answer);
                        calculator3.Multiplication();
                        break;
                    case "4":
                        Console.WriteLine("You chose Division!");
                        Console.WriteLine("Please enter your first number: ");
                        _firstNum = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter your second number: ");
                        _secNum = Convert.ToDouble(Console.ReadLine());
                        Calculations calculator4 = new Calculations(_firstNum, _secNum, _answer);
                        calculator4.Division();
                        break;
                    case "9":
                        Console.WriteLine("Exiting Calculator.");
                        _exit = true;
                        break;
                    default:
                        Console.WriteLine("I don't know what you mean");
                        break;
                }
            }
            return ("Thanks for using my calculator!");
        }
    }
}