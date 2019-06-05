#define  STRICT
#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <string>

#pragma comment(lib, "mpr.lib")

#define BUFFSIZE = 1000

int main( int argc, char *argv[] )
{
    TCHAR szDeviceName[80];
    const char* drive = "F:";
    DWORD dwResult, cchBuff = sizeof(szDeviceName);


// Call the WNetGetConnection function.
//
    dwResult = WNetGetConnection(drive,
                                 szDeviceName,
                                 &cchBuff);

    switch (dwResult)
    {
        //
        // Print the connection name or process errors.
        //
        case NO_ERROR:
            printf("Connection name: %s\n", szDeviceName);
            break;
            //
            // The device is not a redirected device.
            //
        case ERROR_NOT_CONNECTED:
            printf("Device z: not connected.\n");
            break;
            //
            // The device is not currently connected, but it is a persistent connection.
            //
        case ERROR_CONNECTION_UNAVAIL:
            printf("Connection unavailable.\n");
            break;
            //
            // Handle the error.
            //
        default:
            printf("WNetGetConnection failed.\n");
    }
    return 0;
}