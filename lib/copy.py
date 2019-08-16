from notion.block import Block, BasicBlock, TodoBlock, EquationBlock


def copy_block(target: Block, parent: Block):
    copied_block = parent.children.add_new(target.__class__)

    # TODO: colorなどのattributeが失われる

    # special blockについては処理を実施
    if isinstance(target, TodoBlock):
        copied_block.checked = target.checked

    if isinstance(target, EquationBlock):
        copied_block.latex = target.latex

    # BasicBlock
    if isinstance(target, BasicBlock):
        copied_block.title = target.title
        copied_block.color = target.color

    # recursion
    for child in target.children:
        copy_block(child, copied_block)

    return copied_block
