#!/home/raj/.sdkman/candidates/groovy/2.4.12/bin/groovy

String js_content
String html_content
String filename

new File(".").eachFileMatch( ~/^app.*.js$/  ) { file->
    filename = file.getName()          
    js_content = file.getText('UTF-8')   
}

new File(".").eachFileMatch( ~/^index.html$/ ){ file->
    html_content = file.getText('UTF-8')
}

String new_content = html_content.replaceAll(~ /<script type=\"text\/javascript\" src=\"filename\"><\/script>/ , js_content)


println new_content