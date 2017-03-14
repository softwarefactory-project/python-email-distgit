%global sum     Standalone email package

Name:           python-email
Version:        4.0.2
Release:        1%{?dist}
Summary:        %{sum}

License:        Python software Foundation
URL:            http://www.python.org/sigs/email-sig
Source0:        https://pypi.python.org/packages/71/e7/816030d3b0426c130040bd068be62b9213357ed02896f5d9badcf46d1b5f/email-4.0.2.tar.gz

BuildArch:      noarch


%description
This is a standalone version of the version of email package that will ship with Python 3.3. This version can be installed and run under Python3.2. It is intended as a platform for testing the new code, but its final release should also be useable to get the features of the new package under Python 3.2.


%package -n python2-email
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description -n python2-email
This is a standalone version of the version of email package that will ship with Python 3.3. This version can be installed and run under Python3.2. It is intended as a platform for testing the new code, but its final release should also be useable to get the features of the new package under Python 3.2.

%prep
%autosetup -n email-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files


%files -n python2-email
%{python2_sitelib}/email-%{version}-py*.egg-info
%{python2_sitelib}/email


%changelog
* Tue Mar 14 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 4.0.2-1
- Initial packaging
