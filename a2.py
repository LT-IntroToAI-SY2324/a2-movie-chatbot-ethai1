from typing import List

def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """

    source_index = 0  # current index we are looking at in source list
    pattern_index = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)
    while source_index < len(source) or pattern_index < len(pattern):
        # 1) if we reached the end of the pattern but not source
        if pattern_index == len(pattern) - 1 and source_index < len(source) - 1 and pattern[pattern_index] != "%":
            print("PATTERN IS GREATER THAN SOURCE. RETURNING NULL")
            return None
        
        # 2) if the current thing in the pattern is a %
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards

        elif pattern[pattern_index] == "%":
            text: List[str] = []

            if pattern_index > source_index:
                result.append("")
                break

            if pattern_index == len(pattern) - 1:
                while source_index < len(source):
                    text.append(source[source_index])
                    source_index += 1

                joined = " ".join(text)
                result.append(joined)

            else:     
                end_of_pattern = pattern[pattern_index + 1]
                # print(f"END OF PATTERN: {end_of_pattern}")

                while source[source_index] != end_of_pattern:
                    text.append(source[source_index])
                    source_index += 1

                joined = " ".join(text)
                result.append(joined)
            pattern_index += 1
            
        # 3) if we reached the end of the source but not the pattern
        elif source_index == len(source) - 1 and pattern_index < len(pattern) - 1:
            if pattern[pattern_index + 1] != "%":
                print("SOURCE IS LARGER THAN PATTERN. RETURNING NULL")
                return None
        
        # 4) if the current thing in the pattern is an _
        elif pattern[pattern_index] == "_":
            result.append(source[source_index])
            source_index += 1
            pattern_index += 1 

        # 5) if the current thing in the pattern is the same as the current thing in the
        # source
        elif source[source_index] == pattern[pattern_index]:
            source_index += 1
            pattern_index += 1

        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source
        else:
            print("ELSE RETURNING NULL")
            return None

    print(result)
    return result


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed" # FAILED
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed" # FAILED
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
