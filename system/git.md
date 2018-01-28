### restore `commit --amend` to other commit

What you need to do is to create a new commit with the same details as the current HEAD commit, but with the parent as the previous version of HEAD. git reset --soft will move the branch pointer so that the next commit happens on top of a different commit from where the current branch head is now.

```
# Move the current head so that it's pointing at the old commit
# Leave the index intact for redoing the commit.
# HEAD@{1} gives you "the commit that HEAD pointed at before 
# it was moved to where it currently points at". Note that this is
# different from HEAD~1, which gives you "the commit that is the
# parent node of the commit that HEAD is currently pointing to."
git reset --soft HEAD@{1}

# commit the current tree using the commit details of the previous
# HEAD commit. (Note that HEAD@{1} is pointing somewhere different from the
# previous command. It's now pointing at the erroneously amended commit.)
git commit -C HEAD@{1}
```