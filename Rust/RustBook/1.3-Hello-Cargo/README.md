# Hello Cargo

Source: https://doc.rust-lang.org/book/ch01-03-hello-cargo.html

1. Create a new project with `cargo new <project_name>`
   1. Project definitions are saved in `Cargo.toml`
      1. Dependencies are managed automatically in `Cargo.lock`
   2. Source code goes to `src/`
   3. Binaries are saved in `target/`
2. Check (Compile) the code `cargo check`
3. Build the code `cargo build` and manually run `./target/debug/<project_name>`
4. Build and run `cargo run`
5. Release using `cargo build --release` - the binary goes to `./target/release/<project_name>`
