using System;
class HelloWorld {
  static void Main() {
    
    string[] inputs = Console.ReadLine().Split(' ');
    int coins = int.Parse(inputs[0]);
    int mx = int.Parse(inputs[1]);
    
    if (coins * 100 >= mx) {
        Console.WriteLine("Yes");
    }
    else {
        Console.WriteLine("No");
    }
    
  }
}