use std::io::{self, BufRead};

fn solve(s: &str) {
    let n = s.len();
    let mut pi = vec![0; n];
    let mut j = 0;
    for i in 1..n {
        while j > 0 && s.as_bytes()[i] != s.as_bytes()[j] {
            j = pi[j-1];
        }
        if s.as_bytes()[i] == s.as_bytes()[j] {
            j += 1;
            pi[i] = j;
        }
    }
    let k = pi[n-1];
    if n % (n-k) == 0 {
        println!("{}", n / (n-k));
    } else {
        println!("1");
    }
}

fn main() {
    let stdin = io::stdin();
    let lines = stdin.lock().lines().map(Result::unwrap);
    for s in lines {
        if s == "." {
            break;
        }
        solve(&s);
    }
}