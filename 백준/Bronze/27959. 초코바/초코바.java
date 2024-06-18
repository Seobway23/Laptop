import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int coins = scanner.nextInt();
		int mx = scanner.nextInt();
		
		if (coins * 100 >= mx) {
		    System.out.println("Yes");
		}
		else{
		    System.out.println("No");
		}
	}
}