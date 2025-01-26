import jig.cmds.cpp


def test_namespace_list():
    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world")
    ns = cpp._namespace_list()
    assert ns == ["hello", "world"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world::of")
    ns = cpp._namespace_list()
    assert ns == ["hello", "world", "of"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello")
    ns = cpp._namespace_list()
    assert ns == ["hello"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "")
    ns = cpp._namespace_list()
    assert ns == [""]


def test_namespace_rlist():
    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world")
    ns = cpp._namespace_rlist()
    assert ns == ["world", "hello"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world::of")
    ns = cpp._namespace_rlist()
    assert ns == ["of", "world", "hello"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello")
    ns = cpp._namespace_rlist()
    assert ns == ["hello"]

    cpp = jig.cmds.cpp.Cpp("MyClass", "")
    ns = cpp._namespace_rlist()
    assert ns == [""]


def test_include_guard():
    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world")
    assert "HELLO_WORLD_MY_CLASS_HPP" == cpp._include_guard()

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world::of")
    assert "HELLO_WORLD_OF_MY_CLASS_HPP" == cpp._include_guard()

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello")
    assert "HELLO_MY_CLASS_HPP" == cpp._include_guard()

    cpp = jig.cmds.cpp.Cpp("MyClass", "")
    assert "MY_CLASS_HPP" == cpp._include_guard()


def test_include_path():
    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world")
    assert "hello/world/my_class.hpp" == cpp._include_path()

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello::world::of")
    assert "hello/world/of/my_class.hpp" == cpp._include_path()

    cpp = jig.cmds.cpp.Cpp("MyClass", "hello")
    assert "hello/my_class.hpp" == cpp._include_path()

    cpp = jig.cmds.cpp.Cpp("MyClass", "")
    assert "my_class.hpp" == cpp._include_path()
