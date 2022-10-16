For ($i = 0; $i -lt 50; $i++) {
    $obj = new-object -com wscript.shell
    $obj.SendKeys([char]175)
}