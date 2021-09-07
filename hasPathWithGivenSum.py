'''
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

Example

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = true.
'''
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def hasPathWithGivenSum(t, s):
    if t is None:
        return s == 0    
    elif t.left is None and t.right is not None:
        return hasPathWithGivenSum(t.right,s-t.value)
    elif t.right is None and t.left is not None:
        return hasPathWithGivenSum(t.left,s-t.value)
    else:
        return hasPathWithGivenSum(t.left,s-t.value) or hasPathWithGivenSum(t.right,s-t.value)