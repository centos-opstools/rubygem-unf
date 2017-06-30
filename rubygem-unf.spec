# Generated from unf-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unf

Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Group: Development/Languages
License: BSD
URL: https://github.com/knu/ruby-unf
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(shoulda)
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}

%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

#sed -i -e 's/\/usr\/bin\/env rake/\/bin\/rake/g' %{gem_name}-%{version}/Rakefile
sed -i '1d' %{gem_name}-%{version}/Rakefile
chmod 644 %{gem_name}-%{version}/Rakefile

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/unf.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.1.4-1
- Packaged for CentOS

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-5
- F-21 shoulda is now 3.5.0, fix test case

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-3
- Use minitest/autorun instead of minitest/unit

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-2
- Support Minitest 5.x

* Wed Apr  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-1
- 0.1.4

* Sun Oct 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.3-1
- 0.1.3

* Thu Oct  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-1
- 0.1.2

* Mon Apr 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- 0.1.1

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-1
- 0.1.0

* Sat Jan 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.5-1
- Initial package
