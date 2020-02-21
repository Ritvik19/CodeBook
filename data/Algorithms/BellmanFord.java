import java.util.*; 
import java.lang.*; 
import java.io.*; 
import java.util.Scanner;

class BellmanFord { 
    class Edge { 
        int src, dest, weight; 
        Edge() 
        { 
            src = dest = weight = 0; 
        } 
    }; 

    int V, E; 
    Edge edge[]; 

    BellmanFord(int v, int e) 
    { 
        V = v; 
        E = e; 
        edge = new Edge[e]; 
        for (int i = 0; i < e; ++i) 
            edge[i] = new Edge(); 
    } 

    void BellmanFord(BellmanFord graph, int src) 
    { 
        int V = graph.V, E = graph.E; 
        int dist[] = new int[V]; 

        for (int i = 0; i < V; ++i) 
            dist[i] = Integer.MAX_VALUE; 
        dist[src] = 0; 

        for (int i = 1; i < V; ++i) { 
            for (int j = 0; j < E; ++j) { 
                int u = graph.edge[j].src; 
                int v = graph.edge[j].dest; 
                int weight = graph.edge[j].weight; 
                if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) 
                    dist[v] = dist[u] + weight; 
            } 
        } 

        for (int j = 0; j < E; ++j) { 
            int u = graph.edge[j].src; 
            int v = graph.edge[j].dest; 
            int weight = graph.edge[j].weight; 
            if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) { 
                System.out.println("Graph contains negative weight cycle"); 
                return; 
            } 
        } 
        printArr(dist, V); 
    } 

    void printArr(int dist[], int V) 
    { 
        System.out.println("Vertex Distance from Source"); 
        for (int i = 0; i < V; ++i) 
            System.out.println(i + "\t\t" + dist[i]); 
    } 

    public static void main(String[] args) 
    { 
        Scanner inp = new Scanner(System.in); 
        
        System.out.println("Enter number of vertices: ");
        int V = inp.nextInt();
        System.out.println("Enter number of edges: ");
        int E = inp.nextInt();

        BellmanFord graph = new BellmanFord(V, E);

        for(int i=0; i<E; i++)
        {
            System.out.println("Enter Source for Egde"+(i+1)+" :");
            graph.edge[i].src = inp.nextInt();
            System.out.println("Enter Destination for Egde"+(i+1)+" :");
            graph.edge[i].dest = inp.nextInt();
            System.out.println("Enter Weight for Egde"+(i+1)+" :");
            graph.edge[i].weight = inp.nextInt();

        }
        System.out.println("Enter Source to start : ");
		int s = inp.nextInt();

        graph.BellmanFord(graph, s); 
    } 
}