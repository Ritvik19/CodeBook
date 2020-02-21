import java.io.*; 
import java.util.*; 
import java.util.Scanner;

class BreadthFirstSearch 
{ 
	private int V; // No. of vertices 
	private LinkedList<Integer> adj[]; //Adjacency Lists 

	BreadthFirstSearch(int v) 
	{ 
		V = v; 
		adj = new LinkedList[v]; 
		for (int i=0; i<v; ++i) 
			adj[i] = new LinkedList(); 
	} 
 
	void addEdge(int v,int w) 
	{ 
		adj[v].add(w); 
	} 


	void BFS(int s) 
	{ 
 
		boolean visited[] = new boolean[V]; 
		LinkedList<Integer> queue = new LinkedList<Integer>(); 

		visited[s]=true; 
		queue.add(s); 

		while (queue.size() != 0) 
		{ 
			s = queue.poll(); 
			System.out.print(s+" "); 

			Iterator<Integer> i = adj[s].listIterator(); 
			while (i.hasNext()) 
			{ 
				int n = i.next(); 
				if (!visited[n]) 
				{ 
					visited[n] = true; 
					queue.add(n); 
				} 
			} 
		} 
	} 

	public static void main(String args[]) 
	{ 
        Scanner inp = new Scanner(System.in); 

        System.out.println("Enter number of vertices: ");
        int V = inp.nextInt();
        System.out.println("Enter number of edges: ");
        int E = inp.nextInt();

		BreadthFirstSearch graph = new BreadthFirstSearch(V); 

		for(int i=0; i<E; i++)
		{
			System.out.println("Enter source for Edge "+(i+1)+": ");
			int src = inp.nextInt();
			System.out.println("Enter destination for Edge "+(i+1)+": ");
			int des = inp.nextInt();
			graph.addEdge(src, des);
		} 
		System.out.println("Enter Source to start BFS: ");
		int s = inp.nextInt();

		System.out.println("Following is Breadth First Traversal "); 

		graph.BFS(s); 
	} 
} 