# Advent of Code

[![wakatime](https://wakatime.com/badge/user/018c2398-15b4-48fa-922a-a730fce8bcbd/project/018c23e8-2162-4616-8a7e-281d01d40ea2.svg)](https://wakatime.com/badge/user/018c2398-15b4-48fa-922a-a730fce8bcbd/project/018c23e8-2162-4616-8a7e-281d01d40ea2)

This repository reflects the effort I've put into solving advent of code challenges. Here you'll find solutions completed in several languages and varying levels of expertise based on when I solved that challenge.

## AOC CLI

This repository comes equipped with a CLI allowing for easy downloading of new files and setting up new directories for challenges.

Per [AOC Requirements](https://www.reddit.com/r/adventofcode/wiki/faqs/automation/), this script automatically caches input files so they don't need to be read again. It also grabs the test input (if there is one!) and puts it in the same directory.

The easiest way to run a file given its input is:

```bash
$ ./main.py <real.txt
```

This bash syntax pipes the contents of `real.txt` into `./main.py`. Then, you can use `sys.stdin` to read it however you want (via `sys.stdin.readline`, etc.).

> _Of course, you can also use `open("real.txt")` if you want to work with a file pointer and run your script as `./main.py`_.

## Languages

My goal is to solve each challenge using multiple languages to provide the most exposure. The current languages I have solves with:

| **Language** | **Solves** |
| ------------ | ---------- |
| ASM          | 4          |
| Bash         | 7          |
| C            | 28         |
| Python       | 105        |

> _This table is automatically updated using the `aoc` CLI. Sometimes it can be off if a file was accidentally introduced but not fully complete._

Here's a little more about the languages I use:

- **ASM**: x86_64 NASM compiled with Makefile. `glibc` is not used at all - syscalls only!
- **Bash**: Bash v5.2. Not necessarily POSIX compliant. To the greatest extent possible, only using shell built-ins. A future task will be ridding the `aoc` scripts as well.
- **C**: C99 compiled using `gcc`. I was using a library file with a bunch of cheater-functions, but I'm slowly removing its use in favor of solving things the C way.
- **Python**: My speed language I use on challenge day. The only non-default libraries I use (so far) are `numpy` and `networkx`.

# Challenge Calendars

These calendars indicate solves in _at least one_ language.

<table>
<tr>
<td valign="top">

### 2026 Challenges (0/24)

| M   | T   | W   | R   | F   | S   | U   |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |

</td>
<td valign="top">

### 2025 Challenges (24/24)

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: |         |         |

</td>
</tr>
<tr>
<td valign="top">

### 2024 Challenges (50/50)

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: |         |         |         |         |         |

</td>
<td valign="top">

### 2023 Challenges (50/50)

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         |         | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: |         |         |         |         |         |         |

</td>
</tr>

<tr>
<td valign="top">

### 2022 Challenges ( 26/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |

</td>
<td valign="top">

### 2021 Challenges ( 6/50 )

| M   | T   | W       | R       | F       | S   | U   |
| --- | --- | ------- | ------- | ------- | --- | --- |
|     |     | :star2: | :star2: | :star2: |     |     |
|     |     |         |         |         |     |     |
|     |     |         |         |         |     |     |
|     |     |         |         |         |     |     |
|     |     |         |         |         |     |     |

</td>
</tr>

<tr>
<td valign="top">

### 2020 Challenges ( 2/50 )

| M   | T       | W   | R   | F   | S   | U   |
| --- | ------- | --- | --- | --- | --- | --- |
|     | :star2: |     |     |     |     |     |
|     |         |     |     |     |     |     |
|     |         |     |     |     |     |     |
|     |         |     |     |     |     |     |
|     |         |     |     |     |     |     |

</td>
<td valign="top">

### 2019 Challenges ( 2/50 )

| M   | T   | W   | R   | F   | S   | U       |
| --- | --- | --- | --- | --- | --- | ------- |
|     |     |     |     |     |     | :star2: |
|     |     |     |     |     |     |         |
|     |     |     |     |     |     |         |
|     |     |     |     |     |     |         |
|     |     |     |     |     |     |         |

</td>
</tr>

<tr>
<td valign="top">

### 2018 Challenges ( 8/50 )

| M       | T       | W   | R   | F   | S       | U       |
| ------- | ------- | --- | --- | --- | ------- | ------- |
|         |         |     |     |     | :star2: | :star2: |
| :star2: | :star2: |     |     |     |         |         |
|         |         |     |     |     |         |         |
|         |         |     |     |     |         |         |
|         |         |     |     |     |         |         |

</td>
<td valign="top">

### 2017 Challenges ( 2/50 )

| M   | T   | W   | R   | F       | S   | U   |
| --- | --- | --- | --- | ------- | --- | --- |
|     |     |     |     | :star2: |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |
|     |     |     |     |         |     |     |

</td>
</tr>

<tr>
<td valign="top">

### 2016 Challenges ( 16/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         |         |         | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: |         |         |         |         |
| :star2: |         |         |         |         |         |         |
|         |         |         |         |         |         |         |

</td>
<td valign="top">

### 2015 Challenges ( 50/50 )

| M       | T       | W       | R       | F       | S       | U       |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
|         | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: | :star2: | :star2: |
| :star2: | :star2: | :star2: | :star2: | :star2: |         |         |

</td>
</tr>
</table>

> _Key: :star: = silver (pt. 1), :star2: = gold (pt. 1&2)_
