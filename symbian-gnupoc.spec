Summary:	Symbian development on Linux
Summary(pl.UTF-8):	Programowanie na Symbiana na Linuksie
Name:		symbian-gnupoc
Version:	1.07
Release:	1
License:	GPL/distributable
Group:		Developement
Source0:	http://www.martin.st/symbian/gnupoc-package-%{version}.tar.gz
# Source0-md5:	4d3f903c3952b028b54e3ff5c657e527
URL:		http://www.martin.st/symbian/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of patched tools and scripts for compiling them,
for building Symbian applications.

%description -l pl.UTF-8
Kolekcja poprawionych narzędzi i skryptów do ich kompilacji,
umożliwiających budowanie Symbianowych aplikacji.

%prep
%setup -n gnupoc-package-%{version}

%build
cd tools

cd petran-1.1.0
%{__make}
cd ..

cd bmconv-1.1.0-2
%{__make}
cd ..

cd rcomp-7.0.1
%{__make}
cd ..

cd makesis-4
%{__make}
cd ..

cd make-3.81
%configure
%{__make}
cd ..

cd elf2e32
%{__make} -j1 -f Makefile.local-libelf libelf.a elf2e32
cd ..

%{__cxx} mifconv.cpp -o mifconv

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
