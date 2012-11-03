import java.util.*;


public class FirstLambda{
	
	public static void main(String[] args){
		Comparator<Integer> compare = (left, right) -> left > right ? 1 : -1;
		
		System.out.println(compare.compare(2, 1));
		System.out.println(compare.compare(2, 21));

		Run run = () -> {System.out.println("this is run");};
		testRun(run);

		List<String> names = Arrays.asList("Alcce", "Bob", "Charlie");						 
		names.forEach(e -> System.out.println(e));
		//List<String> filterdNames = names.filter(e -> e.length() >= 4).into(new ArrayList<String>());
		//for(String name : filterdNames){
		//	System.out.println(name);
		//}
	}

	public static void testRun(Run r){
		r.run();
	}

	

}

interface Run{
	void run();
}
