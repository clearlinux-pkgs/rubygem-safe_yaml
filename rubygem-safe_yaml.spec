#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-safe_yaml
Version  : 1.0.4
Release  : 5
URL      : https://rubygems.org/downloads/safe_yaml-1.0.4.gem
Source0  : https://rubygems.org/downloads/safe_yaml-1.0.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-safe_yaml-bin
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-hashie
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
SafeYAML
========
[![Build Status](https://travis-ci.org/dtao/safe_yaml.png)](http://travis-ci.org/dtao/safe_yaml)
[![Gem Version](https://badge.fury.io/rb/safe_yaml.png)](http://badge.fury.io/rb/safe_yaml)

%package bin
Summary: bin components for the rubygem-safe_yaml package.
Group: Binaries

%description bin
bin components for the rubygem-safe_yaml package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n safe_yaml-1.0.4
gem spec %{SOURCE0} -l --ruby > rubygem-safe_yaml.gemspec

%build
gem build rubygem-safe_yaml.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
safe_yaml-1.0.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/safe_yaml-1.0.4
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/safe_yaml-1.0.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/README.md
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/bin/safe_yaml
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/bundle_install_all_ruby_versions.sh
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/deep.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/libyaml_checker.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/load.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/parse/date.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/parse/hexadecimal.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/parse/sexagesimal.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/psych_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/psych_resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/safe_to_ruby_visitor.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/syck_hack.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/syck_node_monkeypatch.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/syck_resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_boolean.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_date.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_float.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_nil.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/to_symbol.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/transform/transformation_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/lib/safe_yaml/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/run_specs_all_ruby_versions.sh
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/safe_yaml.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/exploit.1.9.2.yaml
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/exploit.1.9.3.yaml
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/issue48.txt
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/issue49.yml
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/libyaml_checker_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/psych_resolver_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/resolver_specs.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/safe_yaml_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/support/exploitable_back_door.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/syck_resolver_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/transform/base64_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/transform/to_date_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/transform/to_float_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/transform/to_integer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/transform/to_symbol_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/safe_yaml-1.0.4/spec/yaml_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/safe_yaml-1.0.4.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/safe_yaml
