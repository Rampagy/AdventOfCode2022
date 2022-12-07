test 0 = 95437

- / (dir) 48381165
  - a (dir) 94853
    - e (dir) 584
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir) 24933642
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

23447523

test 1 = 189706

- / (dir) 25027911 + 8504156 + 14848514 + 94853 = 48475434
  - a (dir) 94853
    - e (dir) 584
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir) 24933642 +94269 = 25027911
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
    - a (dir) 94269
      - f (file, size=29116)
      - g (file, size=2557)
      - h.lst (file, size=62596)