Summary: 	A curses clone of the classic video game Space Invaders
Name:		ascii-invaders
Version:	0.1b
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.ip9.org/munro/invaders/invaders%{version}.tgz
URL:		http://www.ip9.org/munro/invaders/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses clone of the classic video game Space Invaders.

%prep
%setup -q -n invaders

%build
%{__cc} -c invaders.c -o invaders.o -I%{_includedir}/ncurses
%{__cc} -lncurses invaders.o -o ascii_invaders 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ascii_invaders $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ascii_invaders
