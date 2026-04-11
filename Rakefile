require 'squared'
require 'squared/workspace'
require 'squared/workspace/project/python'

Workspace::Application
  .new
  .with(:python, venv: '.venv', serve: 'build/html', script: false, editable: false) do
    doc(windows? ? '.\make.bat html' : 'make html')
    add(File.basename(Dir.pwd), 'chrome') do
      task('commit:all' => ['lint']) { commit(:all) }
      task('commit:amend' => ['lint']) { commit(:'amend-orig', refs: ['*']) }
    end
  end
  .banner(:path, styles: %i[bright_yellow bold], border: 'bright_blue')
  .style({
    header: %i[bright_yellow bold],
    border: 'bright_blue',
    inline: %i[bright_cyan bold],
    major: %i[bright_magenta bold],
    latest: 'bright_blue'
  })
  .enable_drawing
  .enable_aixterm
  .build

task default: 'commit:all'
