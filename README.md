# Advent of Code

[![wakatime](https://wakatime.com/badge/user/018c2398-15b4-48fa-922a-a730fce8bcbd/project/018c23e8-2162-4616-8a7e-281d01d40ea2.svg)](https://wakatime.com/badge/user/018c2398-15b4-48fa-922a-a730fce8bcbd/project/018c23e8-2162-4616-8a7e-281d01d40ea2)

My solutions for the Advent of Code challenges. The Wakatime badge shows my entire time spent on
this repository. I only started using Wakatime recently, so the time spent on the 2015 (and many
of the 2022) challenges is not included.

# Using this Repository

If you want to download and run this code, you can! You can also use the [aoc](./aoc) program to
run your own AoC repo.

The repo uses the following structure:

```text
.
├── aoc             # Driver script
├── input           # Input files
├── src             # Source files
└── utils           # aoc utility scripts
```

You can get a challenge input using `./aoc fetch <year> <date>` (or calling `./utils/aoc-fetch`
directly). This requires an `AOC_SESSION` environment set, which I have inside
`utils/aoc-session`.

> _Of course, `utils/aoc-session` is gitignored. Also, by request of Eric Wastl (the AoC author),
> the input files are also gitignored._

Then, build an AoC challenge with `./aoc <lang> <year> <date>`. Each supported language uses
its proprietary framework for building.

# Languages

My goal is to solve each challenge using multiple languages to provide the most exposure. The
current languages I have solves with:

| **Language** | **Solves** |
| ------------ | ---------- |
| ASM          | 5          |
| Bash         | 2          |
| C            | 28         |
| Python       | 97         |

> _This table is automatically updated using the [aoc-readme](./utils/aoc-readme) script. It
> only uses the number of existing files to guess-timate this value, so it may be off if unfinished
> challenges were pushed accidentally._

Here's a little more about the languages I use:

- **ASM**: x86_64 NASM compiled with Makefile. `glibc` is not used at all -- syscalls only!
- **Bash**: Bash v5.2. Not necessarily POSIX compliant. To the greatest extent possible, only using shell built-ins. A future task will be ridding the `aoc` scripts as well.
- **C**: C99 compiled with Makefile. To the greatest extent possible, not requiring other linked libraries.
- **Python**: My speed language I use on challenge day. The only non-default libraries I use (so far) are `numpy` and `networkx`.

# Challenge Calendars

These calendars indicate solves in _at least one_ language.

### 2024 Challenges ( 50/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         |         |         |         | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: |         |         |         |         |         |

### 2023 Challenges ( 50/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         |         | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: |         |         |         |         |         |         |

### 2022 Challenges ( 26/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |

### 2021 Challenges ( 0/50 )

### 2020 Challenges ( 0/50 )

### 2019 Challenges ( 0/50 )

### 2018 Challenges ( 0/50 )

### 2017 Challenges ( 2/50 )

| M   | T   | W   | R   | F       | S   | U   |
| --- | --- | --- | --- | ------- | --- | --- |
|     |     |     |     | :star2: |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |

### 2016 Challenges ( 16/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: |         |         |         |         |
| :star2: |         |         |         |         |         |         |
|         |         |         |         |         |         |         |

### 2015 Challenges ( 50/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: |         |         |
