# TODO: optflags
Summary:	Symbian development on Linux
Summary(pl.UTF-8):	Programowanie na Symbiana na Linuksie
Name:		symbian-gnupoc
Version:	1.09
Release:	1
License:	GPL/distributable
Group:		Developement/Tools
Source0:	http://www.martin.st/symbian/gnupoc-package-%{version}.tar.gz
# Source0-md5:	67b86eb218fe390ef0eddf837fbce796
URL:		http://www.martin.st/symbian/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of patched tools and scripts for compiling them,
for building Symbian applications.

%description -l pl.UTF-8
Kolekcja poprawionych narzędzi i skryptów do ich kompilacji,
umożliwiających budowanie aplikacji symbianowych.

%prep
%setup -n gnupoc-package-%{version}

%build
cd tools

%{__make} -C petran-1.1.0
%{__make} -C bmconv-1.1.0-2
%{__make} -C rcomp-7.0.1
%{__make} -C makesis-4

cd make-3.81
%configure
%{__make}
cd ..

%{__make} -C elf2e32 -f Makefile.local-libelf -j1 libelf.a elf2e32

%{__cxx} %{rpmldflags} %{rpmcxxflags} mifconv.cpp -o mifconv

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp tools/petran-1.1.0/e32uid/uidcrc $RPM_BUILD_ROOT%{_bindir}
cp tools/bmconv-1.1.0-2/src/bmconv $RPM_BUILD_ROOT%{_bindir}
cp tools/rcomp-7.0.1/src/rcomp $RPM_BUILD_ROOT%{_bindir}
cp tools/makesis-4/src/{makesis,signsis,makekeys} $RPM_BUILD_ROOT%{_bindir}
cp tools/make-3.81/make $RPM_BUILD_ROOT%{_bindir}/extmake
cp tools/elf2e32/elf2e32 $RPM_BUILD_ROOT%{_bindir}
cp tools/mifconv $RPM_BUILD_ROOT%{_bindir}
ln -s /bin/true $RPM_BUILD_ROOT%{_bindir}/rem
cp tools/del $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
