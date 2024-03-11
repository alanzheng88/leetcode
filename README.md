## VSCode Keybindings

```
{
    "key": "cmd+shift+e",
    "command": "workbench.action.findInFiles",
    "args": {
      "query": "(.*$)",
      "replace": "$1  ",
      "isRegex": true,
    },
    {
      "key": "ctrl+r",
      "command": "-workbench.action.quickOpenNavigateNextInRecentFilesPicker",
      "when": "inQuickOpen && inRecentFilesPicker"
    },
    {
      "key": "ctrl+r",
      "command": "-workbench.action.openRecent"
    },
    {
      "key": "ctrl+r",
      "command": "jupyter.restartkernelandrunallcells"
    }
}
```
