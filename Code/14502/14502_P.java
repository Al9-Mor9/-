import java.util.List;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int map[][];
	static List<Integer[]> virus = new ArrayList<>();
	static int dx[] = {0, 0, 1, -1};
	static int dy[] = {1, -1, 0, 0};
	static Queue<Integer[]> q = new ArrayDeque<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int [N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 2) virus.add(new Integer[] {i, j}); 
			}
		}
		
		//최대 64C3 = 25795이므로 단순히 완전 탐색을 해도 상관 없음
		int ans = comb(0, 0, 0);
		System.out.println(ans);
	}
	
	
	private static int comb(int cnt, int row, int col) {
		if (cnt == 3) {
			return bfs();
		}
		int ccol = col;
		int ans = 0;
		for (int i = row ; i < N; i++) {
			for (int j = col; j < M; j++) {
				if (map[i][j] == 0) {
					map[i][j] = 4;
					col = 0;
					ans = Math.max(comb(cnt + 1, row, ccol), ans);
					map[i][j] = 0;
				}
			}
		}
		return ans;
	}

	private static int bfs() {
		int tmp[][] = new int[N][M];
		for (int i = 0; i < N; i++) tmp[i] = map[i].clone();
		
		for (int i = 0; i < virus.size(); i++) q.offer(virus.get(i));
		while (!q.isEmpty()) {
			Integer[] front = q.poll();
			int x = front[0];
			int y = front[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
				if (tmp[nx][ny] != 0) continue;
				tmp[nx][ny] = 2;
				q.offer(new Integer[] {nx, ny});	
			}
		}

		int ret = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (tmp[i][j] == 0) ret++;
			}
		}
		
		return ret;
	}
	
}
