%define		pkg	npm-registry-client
Summary:	Client for the npm registry
Name:		nodejs-%{pkg}
Version:	0.4.4
Release:	1
License:	BSD
Group:		Development/Libraries
URL:		https://github.com/isaacs/npm-registry-client
# download from https://github.com/isaacs/%{pkg}/tarball/%%{version}
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	36acb8549bbceb4a84fa9d81c1aa39b6
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-chownr < 1
Requires:	nodejs-graceful-fs < 2.1.0
Requires:	nodejs-graceful-fs >= 2.0.0
Requires:	nodejs-mkdirp < 0.4.0
Requires:	nodejs-mkdirp >= 0.3.3
Requires:	nodejs-request < 3
Requires:	nodejs-request >= 2.25.0
Requires:	nodejs-retry = 0.0.6
Requires:	nodejs-rimraf < 3
Requires:	nodejs-rimraf >= 2
Requires:	nodejs-semver < 3.0.0
Requires:	nodejs-semver >= 2.2.1
Requires:	nodejs-slide < 1.2.0
Requires:	nodejs-slide >= 1.1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client for the npm registry.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json index.js lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
