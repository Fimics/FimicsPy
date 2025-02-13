from .karaoke import karaoke_text
"""

Traceback (most recent call last):
  File "/Users/mac/code/python/FimicsPy/sound/filters/vocoder.py", line 1, in <module>
    from .karaoke import karaoke_text
ImportError: attempted relative import with no known parent package
相对导入仅在包内运行时有效，因此你需要以包的方式运行代码，而不是直接运行 vocoder.py。
使用类似这样的命令来运行：
python -m sound.filters.vocoder

"""

if __name__ == '__main__':
    karaoke_text("abc")
