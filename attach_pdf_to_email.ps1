# 正規表現でPDFファイル名から授業の回数を取得
$file_path = $args[0]
$file_path -match "(?<=第).*?(?=回)"
$number = $Matches[0]
if([int]$number -le 9) { # 桁揃え
    $number = "0" + $number
}

# メールの内容
$To = ""
$CC = ""
$Subject = "${subject_number}-report"
$Body = "第${number}回のpdfファイルを提出します。
よろしくお願いいたします。
"


function CreateMailByOutlook {
    $Outlook = New-Object -ComObject Outlook.Application
    $Mail = $Outlook.CreateItem(0)
    $Mail.To = $To
    $Mail.CC = $CC
    $Mail.Subject = $Subject
    $Mail.Body = $Body
    $Mail.Attachments.Add($file_path)
    $inspector = $Mail.GetInspector
    $inspector.Display() # Display() : メールを作成して表示 / Send() : 確認せずに送信
}
 
function Main {
    CreateMailByOutlook
}
 
Main