import java.io.*; 
import java.util.*; 

class DepthFirstSearch 
{ 
	private int V;
	private LinkedList<Integer> adj[]; 

	DepthFirstSearch(int v) 
	{ 
		V = v; 
		adj = new LinkedList[v]; 
		for (int i=0; i<v; ++i) 
			adj[i] = new LinkedList(); 
	} 

	void addEdge(int v, int w) 
	{ 
		adj[v].add(w); // Add w to v's list. 
	} 

	void DFSUtil(int v,boolean visited[]) 
	{  
		visited[v] = true; 
		System.out.print(v+" "); 

		Iterator<Integer> i = adj[v].listIterator(); 
		while (i.hasNext()) 
		{ 
			int n = i.next(); 
			if (!visited[n]) 
				DFSUtil(n, visited); 
		} 
	} 

	void DFS(int v) 
	{ 

		boolean visited[] = new boolean[V]; 

		DFSUtil(v, visited); 
	} 

	public static void main(String args[]) 
	{ 
		Scanner inp = new Scanner(System.in); 

        System.out.println("Enter number of vertices: ");
        int V = inp.nextInt();
        System.out.println("Enter number of edges: ");
        int E = inp.nextInt();

		DepthFirstSearch graph = new DepthFirstSearch(V); 

		for(int i=0; i<E; i++)
		{
			System.out.println("Enter source for Edge "+(i+1)+": ");
			int src = inp.nextInt();
			System.out.println("Enter destination for Edge "+(i+1)+": ");
			int des = inp.nextInt();
			graph.addEdge(src, des);
		} 
		System.out.println("Enter Source to start DFS: ");
		int s = inp.nextInt();

		System.out.println("Following is Depth First Traversal "); 

		graph.DFS(s); 
	} 
}