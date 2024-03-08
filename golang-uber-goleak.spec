# Run tests in check section
%bcond_without check

# https://github.com/uber-go/goleak
%global goipath		go.uber.org/goleak
%global forgeurl	https://github.com/uber-go/goleak
Version:		1.3.0

%gometa

Summary:	Goroutine leak detector
Name:		golang-uber-goleak

Release:	1
Source0:	https://github.com/uber-go/goleak/archive/v%{version}/goleak-%{version}.tar.gz
URL:		https://github.com/uber-go/goleak
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	golang(github.com/stretchr/testify/assert)
%endif
BuildArch:	noarch

%description
Goroutine leak detector to help avoid Goroutine leaks.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n goleak-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

