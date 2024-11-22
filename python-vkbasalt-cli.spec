%global pypi_name vkbasalt-cli
%global module_name vkbasalt

Name:           python-%{pypi_name}
Version:        3.1.1.post2
Release:        1
Summary:        Command line interface for vkBasalt
BuildArch:      noarch

# Code in vkbasalt/lib.py (library) is licensed under lgpl-3.0-only (see COPYING.LGPLv3)
# Code in vkbasalt/cli.py (main program) is licensed under gpl-3.0-only (see COPYING.GPLv3)
License:        LGPL-3.0-only AND GPL-3.0-only
URL:            https://gitlab.com/TheEvilSkeleton/vkbasalt-cli
Source0:        https://files.pythonhosted.org/packages/source/v/pytube/vkbasalt-cli-%{version}.tar.gz

BuildRequires:  python-devel


%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       vkbasalt-cli = %{EVRD}
Requires:       vkbasalt

%description
vkbasalt-cli is a CLI utility and library in conjunction with vkBasalt.
This makes generating configuration files or running vkBasalt with
games easier. This is mainly convenient in environments where
integrating vkBasalt is wishful, for example a GUI application.
Integrating vkbasalt-cli allows a front-end to easily generate and use
specific configurations on the fly, without asking the user to manually
write a configuration file.}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%{_bindir}/%{module_name}
