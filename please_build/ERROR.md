The following is the dependencies for huggingface_hub, as you can see the dependencies branches out quite wide and deep, so manually managing these dependencies is going to very onerous and cumbersome. 

- [huggingface_hub](https://github.com/huggingface/huggingface_hub/blob/25e20ef5b04b00573135450d79a55d2fefa09d83/setup.py#L14)
    - [filelock](https://github.com/tox-dev/py-filelock/blob/main/pyproject.toml#L38)
    - [requests](https://github.com/psf/requests/blob/main/setup.py#L65)
        - charset_normalizer
        - idna
        - urllib3
        - certifi
    - [tqdm>=4.42.1](https://github.com/tqdm/tqdm/blob/master/.meta/requirements-build.txt)
    - ...

While developing on please build, the following is the error I get.

```
plz run //src:main
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/<user>/build_benchmark/please_build/plz-out/bin/src/main.pex/__main__.py", line 395, in <module>
    result = run(explode)
  File "/Users/<user>/build_benchmark/please_build/plz-out/bin/src/main.pex/__main__.py", line 375, in run
    return main()
  File "/Users/<user>/build_benchmark/please_build/plz-out/bin/src/main.pex/__main__.py", line 369, in main
    runpy.run_module(ENTRY_POINT, run_name='__main__')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 228, in run_module
    return _run_code(code, {}, init_globals, run_name, mod_spec)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/src/main.py", line 1, in <module>
    from diffusers import StableDiffusionPipeline
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/diffusers/__init__.py", line 3, in <module>
    from .configuration_utils import ConfigMixin
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/diffusers/configuration_utils.py", line 29, in <module>
    from huggingface_hub import hf_hub_download
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/huggingface_hub/__init__.py", line 305, in __getattr__
    submod = importlib.import_module(submod_path)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/huggingface_hub/file_download.py", line 20, in <module>
    import requests
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/requests/__init__.py", line 147, in <module>
    from . import packages, utils
  File "/var/folders/ws/zw1bj70s2g38pdz_kkp3zzl00000gn/T/pex_j_sctlo4/pex-QZ9dg9Ij4YFJnei3fIUN6FGc5I8/third_party/python/requests/packages.py", line 16, in <module>
    locals()[package] = __import__(package)
ModuleNotFoundError: No module named 'idna'
```