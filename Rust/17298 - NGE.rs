use std::io::{stdin, stdout, Write};

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    input.clear();
    stdin().read_line(&mut input).unwrap();
    let a: Vec<i32> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();

    let mut stack = Vec::new();
    let mut res = vec![-1; n];

    for i in 0..n {
        while let Some(top) = stack.last() {
            if a[*top] < a[i] {
                res[stack.pop().unwrap()] = a[i];
            } else {
                break;
            }
        }
        stack.push(i);
    }

    let mut output = String::new();
    for i in res {
        output.push_str(&format!("{} ", i));
    }
    stdout().write_all(output.as_bytes()).unwrap();
}
