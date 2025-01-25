task :build do
  sh 'python3 -m build'
end

task :install do
  sh 'pip3 install dist/jig-0.1.0-py3-none-any.whl'
end

namespace :dev do
  task :install do
    sh 'pip3 install -e .'
  end
end

task :uninstall do
  sh 'pip3 uninstall jig'
end

task again: %i[uninstall build install]

namespace :b do
  task :project do
    sh 'jig create project app_blub --target build/'
  end

  task :clean do
    rm_rf 'build'
    rm_rf '_build'
  end

  task :p do
    rm_rf 'my_applications'
    sh 'jig create project my_applications --target=. --app MyApp'
    Dir.chdir('my_applications') do
      # Create library within the project"
      sh 'jig create lib AutomatedDriver --target sources'
      sh 'jig create lib HilProtocol --target sources --namespace vector::vt::hil'
      sh 'rake init build'
    end
  end
end
