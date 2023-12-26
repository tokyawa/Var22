use std::io;

// Функция для безопасного чтения вещественных чисел
fn read_float(prompt: &str) -> f64 {
    loop {
        println!("{}", prompt);
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Ошибка чтения строки");
        match input.trim().parse::<f64>() {
            Ok(num) => return num,
            Err(_) => println!("Пожалуйста, введите действительное число."),
        }
    }
}

// Функция для решения биквадратного уравнения
fn solve_biquadratic(a: f64, b: f64, c: f64) -> Vec<f64> {
    if a.abs() < f64::EPSILON {
        vec![]
    } else {
        let d = b * b - 4.0 * a * c;
        if d < 0.0 {
            vec![]
        } else {
            let sqrt_d = d.sqrt();
            let two_a = 2.0 * a;
            let roots = [(-b + sqrt_d) / two_a, (-b - sqrt_d) / two_a];
            roots.iter().filter_map(|&x| {
                if x >= 0.0 {
                    Some(x.sqrt())
                } else {
                    None
                }
            }).flat_map(|x| vec![x, -x]).collect()
        }
    }
}

fn main() {
    let a = read_float("Введите коэффициент a:");
    let b = read_float("Введите коэффициент b:");
    let c = read_float("Введите коэффициент c:");

    let roots = solve_biquadratic(a, b, c);

    if roots.is_empty() {
        println!("Нет действительных корней.");
    } else {
        println!("Корни уравнения: {:?}", roots);
    }
}