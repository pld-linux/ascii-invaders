Summary:	A curses clone of the classic video game Space Invaders
Summary(pl.UTF-8):	Tekstowy klon klasycznej gry wideo Space Invaders
Name:		ascii-invaders
Version:	0.1b
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://www.ip9.org/munro/invaders/invaders%{version}.tgz
# Source0-md5:	fbb3f99a1b198bf4222d26a55665482e
URL:		http://www.ip9.org/munro/invaders/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses clone of the classic video game Space Invaders.

%description -l pl.UTF-8
Jest to oparty o bibliotekę curses klon klasycznej gry wideo Space
Invaders.

%prep
%setup -q -n invaders

%build
%{__cc} %{rpmcflags} -c invaders.c -o invaders.o -I/usr/include/ncurses
%{__cc} %{rpmldflags} invaders.o -o ascii_invaders -lncurses

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ascii_invaders $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ascii_invaders
