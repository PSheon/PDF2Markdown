from core.Util import remove_markdown_warp


def test_remove_markdown_warp():
    assert remove_markdown_warp("```markdown\nHello, world!\n```") == "Hello, world!"
    assert (
        remove_markdown_warp("```markdown\nHello, world!\n```", "markdown")
        == "Hello, world!"
    )
    assert (
        remove_markdown_warp("\n\n```markdown\nHello, world!\n```\n\n", "markdown")
        == "Hello, world!"
    )
    assert (
        remove_markdown_warp(
            "```markdown\nHello, world!\n\\`\\`\\`text\nHi, world!\n\\`\\`\\`\n```",
            "markdown",
        )
        == "Hello, world!\n\\`\\`\\`text\nHi, world!\n\\`\\`\\`"
    )
    assert (
        remove_markdown_warp(
            "\nHello, world!\n\\`\\`\\`text\nHi, world!\n\\`\\`\\`\n", "markdown"
        )
        == "Hello, world!\n\\`\\`\\`text\nHi, world!\n\\`\\`\\`"
    )
    assert (
        remove_markdown_warp("```python\nprint('Hello, world!')\n```", "python")
        == "print('Hello, world!')"
    )
    assert remove_markdown_warp("```bash\nls -l\n```", "bash") == "ls -l"
